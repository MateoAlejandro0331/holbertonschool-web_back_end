import Car from './10-car';

class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    // const { _brand, _motor, _color } = this;
    return new Car();
  }
}

export default EVCar;
