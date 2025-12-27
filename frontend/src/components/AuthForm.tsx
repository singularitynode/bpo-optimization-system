'use client'
import { useState } from 'react'

interface Props {
  onLogin: (username: string, password: string) => void
}

export default function AuthForm({ onLogin }: Props) {
  const [username, setUsername] = useState('admin')
  const [password, setPassword] = useState('admin')
  const [loading, setLoading] = useState(false)
  const [showForgot, setShowForgot] = useState(false)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    onLogin(username, password)
    setTimeout(() => setLoading(false), 2000)  // Sim loading
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-primary to-blue-800 px-4">
      <div className="w-full max-w-md bg-white rounded-xl shadow-2xl p-6 sm:p-8">
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">BPO Enterprise CRM</h1>
          <p className="text-gray-600">Secure Login for Ethical Operations</p>
        </div>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
              required
            />
          </div>
          <button 
            type="submit" 
            disabled={loading}
            className="w-full bg-primary text-white py-2 rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
          >
            {loading ? (
              <>
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Signing in...
              </>
            ) : (
              'Sign In'
            )}
          </button>
        </form>
        <div className="mt-6 text-center space-y-2">
          <button onClick={() => setShowForgot(!showForgot)} className="text-sm text-primary hover:underline">
            Forgot Password?
          </button>
          {showForgot && (
            <p className="text-xs text-gray-500">Contact admin@bpo-stable.com for reset. MFA enabled for prod.</p>
          )}
          <p className="text-xs text-gray-500 mt-2">Default: admin / admin | Enterprise MFA Coming Soon</p>
        </div>
      </div>
    </div>
  )
}