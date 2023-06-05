const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  describe('type SUM', () => {
    it('should return the sum of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 3.7, 4.2), 8);
      assert.strictEqual(calculateNumber('SUM', 2.3, 1.8), 4);
      assert.strictEqual(calculateNumber('SUM', 5.1, 3.9), 9);
    });
  });

  describe('type SUBTRACT', () => {
    it('should return the subtraction of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.7, 3.2), 3);
      assert.strictEqual(calculateNumber('SUBTRACT', 8.2, 2.5), 5);
      assert.strictEqual(calculateNumber('SUBTRACT', 10.9, 4.7), 6);
    });
  });

  describe('type DIVIDE', () => {
    it('should return the division of two rounded numbers', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 10, 2), 5);
      assert.strictEqual(calculateNumber('DIVIDE', 9.4, 3.3), 3);
      assert.strictEqual(calculateNumber('DIVIDE', 15, 3), 5);
    });

    it('should return "Error" if the rounded value of b is 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 10, 0), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 9.5, 0), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 15, 0), 'Error');
    });
  });

  it('should throw an error for invalid type', () => {
    assert.throws(() => calculateNumber('INVALID', 5, 3), Error);
  });
});