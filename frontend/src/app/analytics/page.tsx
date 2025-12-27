'use client'
import { useState, useEffect } from 'react'
import AnalyticsChart from '../../components/AnalyticsChart'
import axios from 'axios'

export default function Analytics() {
  const [analytics, setAnalytics] = useState<any[]>([])
  const [token] = useState(localStorage.getItem('bpo_token') || '')

  useEffect(() => {
    fetchAnalytics()
  }, [])

  const fetchAnalytics = async () => {
    try {
      // Mock/API for user logs (adapt to /metrics)
      const res = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/metrics`, {
        headers: { Authorization: `Bearer ${token}` }
      })
      const mockData = [
        { date: '2025-12-10', logins: 5, sessions: 12, ethics: 98 },
        { date: '2025-12-11', logins: 8, sessions: 15, ethics: 99 },
        { date: '2025-12-12', logins: 6, sessions: 10, ethics: 97 },
      ]
      setAnalytics(mockData)
    } catch (err) {
      console.error('Analytics error:', err)
      setAnalytics([])  // Fallback empty
    }
  }

  return (
    <div className="p-4 sm:p-6 lg:p-8">
      <h1 className="text-xl sm:text-2xl font-bold mb-6">User Analytics</h1>
      {analytics.length > 0 ? (
        <AnalyticsChart data={analytics} />
      ) : (
        <div className="bg-white rounded-lg shadow p-6 text-center">Loading analytics...</div>
      )}
    </div>
  )
}