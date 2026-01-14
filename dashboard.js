window.onload = async () => {
  const token = localStorage.getItem('token')

  if (!token) {
    window.location.href = 'index.html'
    return
  }

  const response = await fetch(`http://127.0.0.1:8000/auth?token=${token}`)

  if (!response.ok) {
    localStorage.removeItem('token')
    window.location.href = 'index.html'
    return
  }

  const logoutButton = document.getElementById('logoutButton')
  if (logoutButton) {
    logoutButton.addEventListener('click', () => {
      localStorage.removeItem('token')
      window.location.href = 'index.html'
    })
  }
}
