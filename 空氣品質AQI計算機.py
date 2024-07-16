def calculate_aqi_single(concentration, pollutant):
    def calculate_aqi_range(concentration, range_values):
        if concentration < 0:
            return None
        for i in range(0, len(range_values) - 1):
            if concentration >= range_values[i] and concentration <= range_values[i + 1]:
                AQI_low, AQI_high, BP_low, BP_high = get_aqi_parameters(i)
                return linear(AQI_low, AQI_high, BP_low, BP_high, concentration)
        return None

    def get_aqi_parameters(index):
        AQI_params = [
            (0, 50, 0, 12),
            (51, 100, 12.1, 35.4),
            (101, 150, 35.5, 55.4),
            (151, 200, 55.5, 150.4),
            (201, 300, 150.5, 250.4),
            (301, 400, 250.5, 350.4),
            (401, 500, 350.5, 500.4)
        ]
        return AQI_params[index]

    def linear(iaqi_low, iaqi_high, bp_low, bp_high, concentration):
        return ((iaqi_high - iaqi_low) / (bp_high - bp_low)) * (concentration - bp_low) + iaqi_low

    def get_aqi_category(aqi):
        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Moderate"
        elif aqi <= 150:
            return "Unhealthy for Sensitive Groups"
        elif aqi <= 200:
            return "Unhealthy"
        elif aqi <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"

    if pollutant == 'PM2.5':
        Range_PM25 = [0, 12, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4]
        AQI_PM25 = calculate_aqi_range(concentration, Range_PM25)
        return AQI_PM25, get_aqi_category(AQI_PM25)
    elif pollutant == 'PM10':
        Range_PM10 = [0, 54, 154, 254, 354, 424, 504, 604]
        AQI_PM10 = calculate_aqi_range(concentration, Range_PM10)
        return AQI_PM10, get_aqi_category(AQI_PM10)
    elif pollutant == 'SO2':
        Range_SO2 = [0, 35, 75, 185, 304, 604, 804, 1004]
        AQI_SO2 = calculate_aqi_range(concentration, Range_SO2)
        return AQI_SO2, get_aqi_category(AQI_SO2)
    else:
        return None, None

def AQI_calculator():
    pollutants = ['PM2.5', 'PM10', 'SO2']
    result = []

    for pollutant in pollutants:
        concentration = float(input(f'Enter the concentration of {pollutant}: '))
        AQI, category = calculate_aqi_single(concentration, pollutant)
        result.append([concentration, f"AQI值：{AQI}", category])

    return result

result = AQI_calculator()
print(result)

