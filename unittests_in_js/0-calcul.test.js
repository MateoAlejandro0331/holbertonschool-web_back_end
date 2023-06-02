const assert = require('assert');
const calculateNumber = require('./0-calcul')

// Test suite
describe('testing calculateNumber', () => {
  // Test cases
  it('result should be 4', () => {
    assert.equal(calculateNumber(3, 1), 4);
  });
  it('result should be 5', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('result should be 5', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('result should be 6', () => {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
  it('result should be 0', () => {
    assert.equal(calculateNumber(-1, 1), 0);
  });
  it('result should be 0', () => {
    assert.equal(calculateNumber(0, 0), 0);
  });
});
