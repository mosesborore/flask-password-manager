
let cpUsername = document.getElementById("copyUsername");

cpUsername.addEventListener("click",

	async function copyUsernameToClipboard() {
		let username = document.getElementById("username");

		text = username.innerText;
		console.log(text);

		if (!navigator.clipboard) {
			// clipboard API not available
			return
		}

		try {
			await navigator.clipboard.writeText(text);
			alert("shortened URL has been copied to the clipboard")

		} catch (err) {
			console.log("Faild to copy", err);
		}
	}

);



let cpPassword = document.getElementById("copyPassword");

cpPassword.addEventListener("click",

	async function copyUsernameToClipboard() {
		let username = document.getElementById("username");

		text = username.innerText;
		console.log(text);

		if (!navigator.clipboard) {
			// clipboard API not available
			return
		}

		try {
			await navigator.clipboard.writeText(text);
			alert("shortened URL has been copied to the clipboard")

		} catch (err) {
			console.log("Faild to copy", err);
		}
	}

);