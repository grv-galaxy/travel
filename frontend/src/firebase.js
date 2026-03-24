import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyCgKYq0NpoElklgIBRKbeO7ZfAWcJrWPdU",
  authDomain: "travel-8f96a.firebaseapp.com",
  projectId: "travel-8f96a",
  storageBucket: "travel-8f96a.firebasestorage.app",
  messagingSenderId: "862981529686",
  appId: "1:862981529686:web:0b9b5f7543eb55533ddbf7",
  measurementId: "G-4E9D17Z6KK"
};

const app = initializeApp(firebaseConfig);
const analytics = getAuth(app);