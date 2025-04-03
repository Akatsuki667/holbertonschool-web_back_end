import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, filename) {
  const user = signUpUser(firstName, lastName);
  const upload = uploadPhoto(filename);

  const promise = await Promise.allSettled([user, upload]);
  return promise.map((promise) => ({
    status: promise.status,
    value: promise.status === 'fulfilled' ? promise.value : `Error: ${promise.reason.message}`,
  }));
}
