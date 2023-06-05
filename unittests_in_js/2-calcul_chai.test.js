const calculateNumber = require('./2-calcul_chai');
const { expect } = require('chai');

describe('calculateNumber', () => {
  describe('type SUM', () => {
    it('should return the sum of two rounded numbers', () => {
      expect(calculateNumber('SUM', 3.7, 4.2)).to.equal(8);
      expect(calculateNumber('SUM', 2.3, 1.8)).to.equal(4);
      expect(calculateNumber('SUM', 5.1, 3.9)).to.equal(9);
    });
  });

  describe('type SUBTRACT', () => {
    it('should return the subtraction of two rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 5.7, 3.2)).to.equal(3);
      expect(calculateNumber('SUBTRACT', 8.2, 2.5)).to.equal(5);
      expect(calculateNumber('SUBTRACT', 10.9, 4.7)).to.equal(6);
    });
  });

  describe('type DIVIDE', () => {
    it('should return the division of two rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 10, 2)).to.equal(5);
      expect(calculateNumber('DIVIDE', 9.4, 3.3)).to.equal(3);
      expect(calculateNumber('DIVIDE', 15, 3)).to.equal(5);
    });

    it('should return "Error" if the rounded value of b is 0', () => {
      expect(calculateNumber('DIVIDE', 10, 0)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 9.5, 0)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 15, 0)).to.equal('Error');
    });
  });

  it('should throw an error for invalid type', () => {
    expect(() => calculateNumber('INVALID', 5, 3)).to.throw('Invalid type');
  });
});