# ES6 Promises

## 0. Keep every promise you make and only make promises you can keep
- Return a Promise using this prototype function `getResponseFromAPI()`

## 1. Don't make a promise...if you know you can't keep it
- Using the prototype below, return a `promise`. The parameter is a `boolean`.

## 2. Catch me if you can!
- Using the function prototype below

## 3. Handle multiple successful promises
- In this file, import `uploadPhoto` and `createUser` from `utils.js`
- Knowing that the functions in `utils.js` return promises, use the prototype below to collectively resolve all promises and log `body firstName lastName` to the console.

## 4. Simple promise
- Using the following prototype

## 5. Reject the promises
- Write and export a function named `uploadPhoto`. It should accept one argument `fileName` (string).
- The function should return a Promise rejecting with an Error and the string `$fileName cannot be processed`

## 6. Handle multiple promises
- Import `signUpUser` from `4-user-promise.js` and `uploadPhoto` from `5-photo-reject.js`.
- Write and export a function named `handleProfileSignup`. It should accept three arguments `firstName` (string), `lastName` (string), and `fileName` (string). The function should call the two other functions. When the promises are all settled it should return an array with the following structure:
