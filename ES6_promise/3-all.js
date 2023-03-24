import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const value = `${results[0].body} ${results[1].firstName} ${results[1].lastName}`;
      console.log(value);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
