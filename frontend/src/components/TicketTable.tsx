'use client'
import { useState } from 'react'

interface Ticket {
  ticket_id: string
  task: string
  status: string
  qa_score: number
}

interface Props {
  tickets: Ticket[]
  onProcess: (prompt: string) => void
}

export default function TicketTable({ tickets, onProcess }: Props) {
  const [newPrompt, setNewPrompt] = useState('')

  return (
    <div className="bg-white rounded-lg shadow overflow-hidden">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-2 sm:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
            <th className="px-2 sm:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Task</th>
            <th className="px-2 sm:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            <th className="px-2 sm:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">QA Score</th>
            <th className="px-2 sm:px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {tickets.map((ticket) => (
            <tr key={ticket.ticket_id} className="hover:bg-gray-50">
              <td className="px-2 sm:px-6 py-4 whitespace-nowrap text-sm text-gray-900">{ticket.ticket_id}</td>
              <td className="px-2 sm:px-6 py-4 text-sm text-gray-900 max-w-xs truncate">{ticket.task}</td>
              <td className="px-2 sm:px-6 py-4 whitespace-nowrap text-sm text-gray-900">{ticket.status}</td>
              <td className="px-2 sm:px-6 py-4 whitespace-nowrap text-sm text-gray-900">{ticket.qa_score}</td>
              <td className="px-2 sm:px-6 py-4 whitespace-nowrap text-sm font-medium">
                <button className="text-primary hover:text-blue-500 text-xs sm:text-sm">Edit</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="p-4 border-t flex flex-col sm:flex-row gap-2">
        <input
          type="text"
          value={newPrompt}
          onChange={(e) => setNewPrompt(e.target.value)}
          placeholder="New ticket prompt..."
          className="flex-1 border rounded px-2 py-1 text-sm"
        />
        <button onClick={() => { onProcess(newPrompt); setNewPrompt(''); }} className="bg-secondary text-white px-4 py-1 rounded text-sm">
          Process
        </button>
      </div>
    </div>
  )
}