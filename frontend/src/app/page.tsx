'use client'
import { useState, useEffect } from 'react'
import Dashboard from '../components/Dashboard'
import AuthForm from '../components/AuthForm'
import axios from 'axios'

export default function Home() {
  const [token, setToken] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const storedToken = localStorage.getItem('bpo_token')
    if (storedToken) setToken(storedToken)
    setLoading(false)
  }, [])

  const handleLogin = async (username: string, password: string) => {
    try {
      const res = await axios.post(`${process.env.NEXT_PUBLIC_BACKEND_URL}/token`, { username, password })
      const newToken = res.data.access_token
      localStorage.setItem('bpo_token', newToken)
      setToken(newToken)
    } catch (err) {
      alert('Login failed')
    }
  }

  if (loading) return <div className="flex justify-center items-center h-screen bg-gray-100">Loading...</div>

  return (
    <main className="min-h-screen bg-gray-100">
      {!token ? (
        <AuthForm onLogin={handleLogin} />
      ) : (
        <Dashboard token={token} onLogout={() => { localStorage.removeItem('bpo_token'); setToken(null); }} />
      )}
    </main>
  )
}