const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  let calculateNumberStub;
  let consoleLogSpy;

  beforeEach(() => {
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleLogSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });

  it('should use Utils.calculateNumber stub with type SUM, a = 100, and b = 20', () => {
    sendPaymentRequestToApi(100, 20);
    expect(calculateNumberStub.calledOnceWith('SUM', 100, 20)).to.be.true;
  });

  it('should log the correct message with the stubbed result', () => {
    sendPaymentRequestToApi(100, 20);
    expect(consoleLogSpy.calledOnceWith('The total is: 10')).to.be.true;
  });
});