function samle_data () {
    teller += 1
    analog_NTC = pins.analogReadPin(AnalogReadWritePin.P10)
    spenning_NTC = analog_NTC / 1023 * Uref
    temperatur_NTC = 39.7956 * spenning_NTC - 42.7499
    trykk = BME280.pressure(BME280_P.Pa)
    luftfuktighet = BME280.humidity()
    duggpunkt = BME280.Dewpoint()
    pxtlora.e32SendString("")
    az = GY91.akselerasjon(GY91.Akse.Z)
    ay = GY91.akselerasjon(GY91.Akse.Y)
    ax = GY91.akselerasjon(GY91.Akse.X)
    gz = GY91.gyro(GY91.Akse.Z)
    gy = GY91.gyro(GY91.Akse.Y)
    gx = GY91.gyro(GY91.Akse.X)
    mz = GY91.magnetfelt(GY91.Akse.Z)
    my = GY91.magnetfelt(GY91.Akse.Y)
    mx = GY91.magnetfelt(GY91.Akse.X)
    CO2 = SGP30.eCO2()
    TVOC = SGP30.TVOC()
    hel_frembak = GY91.helning(GY91.Helning.ForoverBakover)
    hel_side = GY91.helning(GY91.Helning.Sideveis)
    hel_retning = GY91.helning(GY91.Helning.Sideveis)
}
function avrund (verdi: number, faktor: number) {
    faktor = 10 ** faktor
    return Math.round(verdi * faktor) / faktor
}
input.onButtonPressed(Button.A, function () {
    GY91.setMagOffset(14, 34, -69)
    SGP30.setClimateCompensation(temperatur_NTC, BME280.humidity())
    GY91.kalibrerGyro()
    GY91.nullstillYaw()
})
function vise_data_OLED () {
    kitronik_VIEW128x64.clear()
    kitronik_VIEW128x64.show("Spenning (NTC): " + ("" + avrund(spenning_NTC, 3)) + " V")
}
input.onButtonPressed(Button.AB, function () {
    datalogging.deleteLog()
})
function logge_data () {
    datalogging.log(
    datalogging.createCV("Teller", teller),
    datalogging.createCV("Temperatur (NTC)", avrund(temperatur_NTC, 1)),
    datalogging.createCV("Spenning (NTC)", spenning_NTC),
    datalogging.createCV("Trykk", trykk),
    datalogging.createCV("Luftfuktighet", luftfuktighet),
    datalogging.createCV("Duggpunkt", duggpunkt),
    datalogging.createCV("Ax", ax),
    datalogging.createCV("Ay", ay),
    datalogging.createCV("Az", az),
    datalogging.createCV("Gx", gx),
    datalogging.createCV("Gy", gy),
    datalogging.createCV("Gz", gz),
    datalogging.createCV("Mx", mx),
    datalogging.createCV("My", my),
    datalogging.createCV("Mz", mz),
    datalogging.createCV("CO2", CO2),
    datalogging.createCV("TVOC", TVOC),
    datalogging.createCV("Hel (Frem/Bak)", hel_frembak),
    datalogging.createCV("Hel (Side)", hel_side),
    datalogging.createCV("Hel (retning)", hel_retning)
    )
}
function vise_data_PC () {
    let tid_UTC = 0
    let fart_km_t = 0
    let lengdegrad = 0
    let breddegrad = 0
    serial.writeValue("Teller", teller)
    serial.writeValue("Temperatur (NTC)", avrund(temperatur_NTC, 1))
    serial.writeValue("Trykk", trykk)
    serial.writeValue("Luftfuktighet", luftfuktighet)
    serial.writeValue("Duggpunkt", duggpunkt)
    serial.writeValue("Ax", ax)
    serial.writeValue("Ay", ay)
    serial.writeValue("Az", az)
    serial.writeValue("Gx", gx)
    serial.writeValue("Gy", gy)
    serial.writeValue("Gz", gz)
    serial.writeValue("Mx", mx)
    serial.writeValue("My", my)
    serial.writeValue("Mz", mz)
    serial.writeValue("CO2", CO2)
    serial.writeValue("TVOC", TVOC)
    serial.writeValue("Breddegrad", breddegrad)
    serial.writeValue("Lengdegrad", lengdegrad)
    serial.writeValue("Fart (km/t)", fart_km_t)
    serial.writeValue("Tid (UTC)", tid_UTC)
}
let faktor = 0
let hel_retning = 0
let hel_side = 0
let hel_frembak = 0
let TVOC = 0
let CO2 = 0
let mx = 0
let my = 0
let mz = 0
let gx = 0
let gy = 0
let gz = 0
let ax = 0
let ay = 0
let az = 0
let duggpunkt = 0
let luftfuktighet = 0
let trykk = 0
let temperatur_NTC = 0
let spenning_NTC = 0
let analog_NTC = 0
let teller = 0
let Uref = 0
let faktor22 = 0
let faktor2 = 0
kitronik_VIEW128x64.show("Verden")
BME280.PowerOn()
BME280.Address(BME280_I2C_ADDRESS.ADDR_0x76)
SGP30.init()
Uref = 3.2
basic.forever(function () {
    samle_data()
    logge_data()
    vise_data_OLED()
    vise_data_PC()
    basic.pause(500)
})
