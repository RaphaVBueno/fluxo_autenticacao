const loginForm = document.getElementById('loginForm')

loginForm.addEventListener('submit', async (e) => {
  e.preventDefault()

  const email = document.getElementById('loginEmail').value
  const password = document.getElementById('loginPassword').value

  try {
    const response = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    })

    const data = await response.json()

    if (response.ok) {
      localStorage.setItem('token', data.access_token)
      window.location.href = 'dashboard.html'
    } else {
      alert(`Erro: ${data.detail || 'Falha ao logar'}`)
    }
  } catch (error) {
    console.error(error)
    alert('Erro de conexão com o servidor')
  }
})
