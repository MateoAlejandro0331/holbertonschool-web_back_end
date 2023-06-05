const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');

describe('API', () => {
  describe('GET /', () => {
    it('should return the correct status code', async () => {
      const response = await request(app).get('/');
      expect(response.status).to.equal(200);
    });

    it('should return the correct result', async () => {
      const response = await request(app).get('/');
      expect(response.text).to.equal('Welcome to the payment system');
    });
  });
});