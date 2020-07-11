importScripts('https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js');
  const firebaseConfig = {
  apiKey: "AIzaSyBIzEO9_QSfcZ0nUbtj-JGO8DNIPDUep30",
  authDomain: "savegreen-885e0.firebaseapp.com",
  databaseURL: "https://savegreen-885e0.firebaseio.com",
  projectId: "savegreen-885e0",
  storageBucket: "savegreen-885e0.appspot.com",
  messagingSenderId: "283130365789",
  appId: "1:283130365789:web:0da986f1c5d00981c14ab4"
};

firebase.initializeApp(firebaseConfig);
const messaging=firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
    console.log(payload);
    const notification=JSON.parse(payload);
    const notificationOption={
        body:notification.body,
        icon:notification.icon
    };
    return self.registration.showNotification(payload.notification.title,notificationOption);
});