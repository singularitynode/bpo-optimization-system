import { NextRequest, NextResponse } from 'next/server'
import axios from 'axios'

export async function POST(req: NextRequest) {
  try {
    const body = await req.json()
    const backendRes = await axios.post(`${process.env.BACKEND_URL || 'http://localhost:8000'}/cycle`, body, {
      headers: { Authorization: req.headers.get('Authorization') || '' }
    })
    return NextResponse.json(backendRes.data)
  } catch (err) {
    return NextResponse.json({ error: 'Proxy failed' }, { status: 500 })
  }
}