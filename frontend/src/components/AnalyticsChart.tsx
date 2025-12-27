'use client'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

interface Props {
  data: any[]
}

export default function AnalyticsChart({ data }: Props) {
  return (
    <div className="bg-white rounded-lg shadow p-4 sm:p-6">
      <h3 className="text-lg font-semibold mb-4">User Activity Trends</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="logins" stroke="#3B82F6" name="Logins" />
          <Line type="monotone" dataKey="sessions" stroke="#10B981" name="Sessions" />
          <Line type="monotone" dataKey="ethics" stroke="#EF4444" name="Ethics %" />
        </LineChart>
      </ResponsiveContainer>
      <div className="mt-4 grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
        <div className="text-center bg-gray-50 p-2 rounded">Total Users: {data.reduce((sum, d) => sum + d.logins, 0)}</div>
        <div className="text-center bg-gray-50 p-2 rounded">Avg Session: {data.reduce((sum, d) => sum + d.sessions, 0) / data.length}</div>
        <div className="text-center bg-gray-50 p-2 rounded">Ethics Avg: {data.reduce((sum, d) => sum + d.ethics, 0) / data.length}%</div>
      </div>
    </div>
  )
}