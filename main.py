def samle_data():
    global teller, analog_NTC, spenning_NTC, temperatur_NTC, trykk, luftfuktighet, duggpunkt, az, ay, ax, gz, gy, gx, mz, my, mx, CO2, TVOC, hel_frembak, hel_side, hel_retning
    teller += 1
    analog_NTC = pins.analog_read_pin(AnalogReadWritePin.P10)
    spenning_NTC = analog_NTC / 1023 * Uref
    temperatur_NTC = 39.7956 * spenning_NTC - 42.7499
    trykk = BME280.pressure(BME280_P.PA)
    luftfuktighet = BME280.humidity()
    duggpunkt = BME280.dewpoint()
    pxtlora.e32_send_string("")
    az = GY91.akselerasjon(GY91.Akse.Z)
    ay = GY91.akselerasjon(GY91.Akse.Y)
    ax = GY91.akselerasjon(GY91.Akse.X)
    gz = GY91.gyro(GY91.Akse.Z)
    gy = GY91.gyro(GY91.Akse.Y)
    gx = GY91.gyro(GY91.Akse.X)
    mz = GY91.magnetfelt(GY91.Akse.Z)
    my = GY91.magnetfelt(GY91.Akse.Y)
    mx = GY91.magnetfelt(GY91.Akse.X)
    CO2 = SGP30.e_co2()
    TVOC = SGP30.TVOC()
    hel_frembak = GY91.helning(GY91.Helning.FOROVER_BAKOVER)
    hel_side = GY91.helning(GY91.Helning.SIDEVEIS)
    hel_retning = GY91.helning(GY91.Helning.SIDEVEIS)
def avrund(verdi: number, faktor: number):
    faktor = 10 ** faktor
    return Math.round(verdi * faktor) / faktor

def on_button_pressed_a():
    GY91.set_mag_offset(14, 34, -69)
    SGP30.set_climate_compensation(temperatur_NTC, BME280.humidity())
    GY91.kalibrer_gyro()
    GY91.nullstill_yaw()
input.on_button_pressed(Button.A, on_button_pressed_a)

def vise_data_OLED():
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("Spenning (NTC): " + ("" + str(avrund(spenning_NTC, 3))) + " V")

def on_button_pressed_ab():
    datalogging.delete_log()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def logge_data():
    datalogging.log(datalogging.create_cv("Teller", teller),
        datalogging.create_cv("Temperatur (NTC)", avrund(temperatur_NTC, 1)),
        datalogging.create_cv("Spenning (NTC)", spenning_NTC),
        datalogging.create_cv("Trykk", trykk),
        datalogging.create_cv("Luftfuktighet", luftfuktighet),
        datalogging.create_cv("Duggpunkt", duggpunkt),
        datalogging.create_cv("Ax", ax),
        datalogging.create_cv("Ay", ay),
        datalogging.create_cv("Az", az),
        datalogging.create_cv("Gx", gx),
        datalogging.create_cv("Gy", gy),
        datalogging.create_cv("Gz", gz),
        datalogging.create_cv("Mx", mx),
        datalogging.create_cv("My", my),
        datalogging.create_cv("Mz", mz),
        datalogging.create_cv("CO2", CO2),
        datalogging.create_cv("TVOC", TVOC),
        datalogging.create_cv("Hel (Frem/Bak)", hel_frembak),
        datalogging.create_cv("Hel (Side)", hel_side),
        datalogging.create_cv("Hel (retning)", hel_retning))
def vise_data_PC():
    tid_UTC = 0
    fart_km_t = 0
    lengdegrad = 0
    breddegrad = 0
    serial.write_value("Teller", teller)
    serial.write_value("Temperatur (NTC)", avrund(temperatur_NTC, 1))
    serial.write_value("Trykk", trykk)
    serial.write_value("Luftfuktighet", luftfuktighet)
    serial.write_value("Duggpunkt", duggpunkt)
    serial.write_value("Ax", ax)
    serial.write_value("Ay", ay)
    serial.write_value("Az", az)
    serial.write_value("Gx", gx)
    serial.write_value("Gy", gy)
    serial.write_value("Gz", gz)
    serial.write_value("Mx", mx)
    serial.write_value("My", my)
    serial.write_value("Mz", mz)
    serial.write_value("CO2", CO2)
    serial.write_value("TVOC", TVOC)
    serial.write_value("Breddegrad", breddegrad)
    serial.write_value("Lengdegrad", lengdegrad)
    serial.write_value("Fart (km/t)", fart_km_t)
    serial.write_value("Tid (UTC)", tid_UTC)
faktor2 = 0
hel_retning = 0
hel_side = 0
hel_frembak = 0
TVOC = 0
CO2 = 0
mx = 0
my = 0
mz = 0
gx = 0
gy = 0
gz = 0
ax = 0
ay = 0
az = 0
duggpunkt = 0
luftfuktighet = 0
trykk = 0
temperatur_NTC = 0
spenning_NTC = 0
analog_NTC = 0
teller = 0
Uref = 0
faktor22 = 0
kitronik_VIEW128x64.show("" + "Verden")
BME280.power_on()
BME280.address(BME280_I2C_ADDRESS.ADDR_0X76)
SGP30.init()
Uref = 3.2

def on_forever():
    samle_data()
    logge_data()
    vise_data_OLED()
    vise_data_PC()
    basic.pause(500)
basic.forever(on_forever)
