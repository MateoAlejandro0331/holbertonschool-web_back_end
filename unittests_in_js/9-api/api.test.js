const chai = require('chai');
const expect = chai.expect;
const request = require('request');

describe('API', () => {
  describe('GET /', () => {
    it('should return 200', (done) => {
      request('http://localhost:7865', (err, res) => {
        expect(res.statusCode).to.equal(200);
        done();
      });
    });

    it('should return the correct result', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });

  describe('GET /cart/:id', () => {
    it('should return 200 when :id is a number', (done) => {
      request('http://localhost:7865/cart/123', (err, res) => {
        expect(res.statusCode).to.equal(200);
        done();
      });
    });

    it('should return the correct result when :id is a number', (done) => {
      request('http://localhost:7865/cart/1', (err, res, body) => {
        expect(body).to.equal('Payment methods for cart 1');
        done();
      });
    });

    it('should return 404 when :id is NOT a number', (done) => {
      request('http://localhost:7865/cart/abc', (err, res) => {
        expect(res.statusCode).to.equal(404);
        done();
      });
    });
  });
});