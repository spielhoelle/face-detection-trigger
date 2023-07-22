export const action = async (side) => {
	try {
		const res = await fetch('http://127.0.0.1:8000/faceactions/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ side })
		})
		const data = await res.json()
		return data
	} catch (error) {
		return error
	}
}