'use client'
import { useState } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import Link from 'next/link'

interface Props {
  token: string
  onLogout: () => void
}

export default function Dashboard({ token, onLogout }: Props) {
  const [data] = useState([
    { name: 'Mon', stability: 99, ethics: 98 },
    { name: 'Tue', stability: 99.5, ethics: 97.5 },
    { name: 'Wed', stability: 100, ethics: 99 },
  ])

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6 p-4 sm:p-6 lg:p-8">
      <div className="col-span-2 bg-white rounded-lg shadow p-4 sm:p-6">
        <h2 className="text-lg sm:text-xl font-semibold mb-4">System Metrics</h2>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="stability" stroke="#3B82F6" />
            <Line type="monotone" dataKey="ethics" stroke="#10B981" />
          </LineChart>
        </ResponsiveContainer>
      </div>
      <div className="bg-white rounded-lg shadow p-4 sm:p-6">
        <h2 className="text-lg sm:text-xl font-semibold mb-4">Quick Actions</h2>
        <Link href="/tickets" className="block mb-2 p-2 bg-primary text-white rounded hover:bg-blue-600 text-sm sm:text-base">View Tickets</Link>
        <Link href="/analytics" className="block mb-2 p-2 bg-secondary text-white rounded hover:bg-green-600 text-sm sm:text-base">User Analytics</Link>
        <button onClick={onLogout} className="w-full p-2 bg-red-500 text-white rounded hover:bg-red-600 text-sm sm:text-base">Logout</button>
      </div>
    </div>
  )
}