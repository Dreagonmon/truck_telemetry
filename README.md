# truck-telemetry
using [scs-sdk-plugin by RenCloud](https://github.com/RenCloud/scs-sdk-plugin)

SCS Telemetry for EuroTruckSimulator 2 and AmericanTruckSimulator

## Supported Version
Current supported [scs-sdk-plugin V.1.10.6](https://github.com/RenCloud/scs-sdk-plugin/releases/tag/V.1.10.6)

## Useage
Download supported version scs-sdk-plugin, and follow the [guide](https://github.com/RenCloud/scs-sdk-plugin#installation) to install.

```pip install truck-telemetry```

```python
import truck_telemetry
truck_telemetry.init()
# read data, it`s slow... cache what you need.
data = truck_telemetry.get_data() # type: dict
# using data
speed = data["speed"] # type: float
```

More dict keys: [scs-telemetry-common.hpp(V.1.10.6)](https://github.com/RenCloud/scs-sdk-plugin/blob/V.1.10.6/scs-telemetry/inc/scs-telemetry-common.hpp)