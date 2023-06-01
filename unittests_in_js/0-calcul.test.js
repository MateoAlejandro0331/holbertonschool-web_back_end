const assert = require('assert');
const calculateNumber = require('./0-calcul')

// Test suite
describe('testing calculateNumber', () => {
  // Test cases
  it('result should be 4', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('result should be 5', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('result should be 5', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('result should be 6', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('result should be 1', () => {
    assert.strictEqual(calculateNumber(-1, 2), 1);
  });

  it('result should be 0', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });
});