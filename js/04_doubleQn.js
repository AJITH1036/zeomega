let firstName = null;
let lastName = null;
let nickName = "Supercoder";

// console.log(firstName ?? lastName ?? nickName ?? "Anonymous"); // Supercoder

// shows the first truthy value:
console.log(firstName || lastName || nickName || "Anonymous"); // Supercoder