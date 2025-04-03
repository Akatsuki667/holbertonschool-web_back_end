export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const success = true;
    if (success === true) {
      resolve();
    } else {
      reject();
    }
  });
}
