const registerForm = document.getElementById('registerForm')

registerForm.addEventListener('submit', async (e) => {
  e.preventDefault()

  const email = document.getElementById('registerEmail').value
  const password = document.getElementById('registerPassword').value
  const passwordConfirm = document.getElementById(
    'registerPasswordConfirm'
  ).value

  if (password !== passwordConfirm) {
    alert('As senhas não coincidem')
    return
  }

  try {
    const response = await fetch('http://127.0.0.1:8000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    })

    const data = await response.json()

    if (response.ok) {
      alert('Usuário cadastrado com sucesso!')
      window.location.href = 'index.html'
    } else {
      alert(`Erro: ${data.detail || 'Falha ao registrar'}`)
    }
  } catch (error) {
    console.error(error)
    alert('Erro de conexão com o servidor')
  }
})
