import singUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const result = [];
  await singUpUser(firstName, lastName).then((response) => { // wait till response is received
    result.push({ status: 'fulfilled', value: response });
  })
    .catch((err) => {
      result.push({ status: 'rejected', value: `Error: ${err.message}` });
    });

  await uploadPhoto(fileName).then((response) => {
    result.push({ status: 'fulfilled', value: response });
  }).catch((err) => {
    result.push({ status: 'rejected', value: `Error: ${err.message}` });
  });
  return result;
}
