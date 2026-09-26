import { uploadUser, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadUser(), createUser()])
    .then(([photo, user]) => {
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
