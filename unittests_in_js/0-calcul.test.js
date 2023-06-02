const assert = require('assert');
const calculateNumber = require('./0-calcul')

// Test suite
describe('testing calculateNumber', () => {
  // Test cases
  it('result should be 4', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });

  it('result should be 5', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });

  it('result should be 6', () => {
    assert.equal(calculateNumber(1.6, 3.7), 6);
  });

  it('result should be 5', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
});