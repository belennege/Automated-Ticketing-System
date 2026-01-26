# Developer Documentation

## File Structure

## Code Overview
- `main.py`: Handles input, validation, fare calculation, output
- `stations.py`: Dictionary of stations and zones
- `fare_calculator.py`: Calculates zones crossed and fare
- `validation.py`: Checks if station exists

## Adding New Stations/Zones
- Update `stations.py`:
```python
stations = {
    "Central": 1,
    "Northside": 2,
    "NewStation": 3
}
