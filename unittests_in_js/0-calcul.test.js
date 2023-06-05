const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return the sum of two rounded numbers', () => {
    assert.strictEqual(calculateNumber(3.7, 4.2), 8);
    assert.strictEqual(calculateNumber(2.3, 1.8), 4);
    assert.strictEqual(calculateNumber(5.1, 3.9), 9);
  });
});
