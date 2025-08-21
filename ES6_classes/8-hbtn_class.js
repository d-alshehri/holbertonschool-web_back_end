// 8-hbtn_class.js
export default class HolbertonClass {
    constructor(size, location) {
      this._size = size;
      this._location = location;
    }
  
    // When cast to Number, return size
    valueOf() {
      return this._size;
    }
  
    // When cast to String, return location
    toString() {
      return this._location;
    }
  }
  