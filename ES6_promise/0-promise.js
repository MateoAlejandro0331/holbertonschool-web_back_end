export default function getResponseFromAPI() {
  const promise = new Promise((resolve, reject) => {
    const response = true;
    if (response) {
      resolve();
    } else {
      reject(new Error('Operation failed'));
    }
  });
  return promise;
}
