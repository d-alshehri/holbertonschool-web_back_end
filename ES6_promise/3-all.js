import { uploadPhoto, createUser } from './utils.js';
export default function handleProfileSignup(){
    const photoPromise = uploadPhoto();
    const userPromise = createUser();

    return Promise.all([photoPromise, userPromise])
        .then(([photoResult, userResult]) => {
            console.log(body, firstName, lastName)
        })
        .catch(()=> {
            console.log("Signup system offline");
        })
}
