'use client'
import { useState, useEffect } from 'react'
import TicketTable from '../../components/TicketTable'
import axios from 'axios'

export default function Tickets() {
  const [tickets, setTickets] = useState<any[]>([])
  const [token] = useState(localStorage.getItem('bpo_token') || '')

  useEffect(() => {
    fetchTickets()
  }, [])

  const fetchTickets = async () => {
    try {
      const res = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/cycle`, {
        headers: { Authorization: `Bearer ${token}` }
      })
      setTickets(res.data.result || [])
    } catch (err) {
      console.error('Fetch error:', err)
    }
  }

  const handleProcess = async (prompt: string) => {
    try {
      const res = await axios.post(`${process.env.NEXT_PUBLIC_BACKEND_URL}/cycle`, { prompt }, {
        headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' }
      })
      fetchTickets()
      alert(`Processed: ${res.data.result.ticket_id}`)
    } catch (err) {
      alert('Process failed')
    }
  }

  return (
    <div className="p-4 sm:p-6 lg:p-8">
      <h1 className="text-xl sm:text-2xl font-bold mb-4">Tickets Dashboard</h1>
      <TicketTable tickets={tickets} onProcess={handleProcess} />
    </div>
  )
}