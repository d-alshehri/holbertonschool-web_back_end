// 10-car.js
export default class Car {
    constructor(brand, motor, color) {
      this._brand = brand;
      this._motor = motor;
      this._color = color;
    }
  
    // Method to clone the current car instance
    cloneCar() {
      // Use this.constructor to create a new instance of the same class
      return new this.constructor(this._brand, this._motor, this._color);
    }
  }
  