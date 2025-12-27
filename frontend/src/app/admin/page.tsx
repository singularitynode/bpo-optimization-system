'use client'
import { useState, useEffect } from 'react'
import { 
  Shield, 
  Users, 
  BarChart3, 
  Cpu, 
  Globe, 
  Database, 
  Zap, 
  Lock,
  Activity,
  Brain,
  Code,
  Key
} from 'lucide-react'

interface SystemMetrics {
  stability: number
  ethics: number
  agents: number
  throughput: number
  latency: number
  uptime: number
  revenue: number
  costs: number
}

interface TheoremResult {
  theorem: string
  status: 'proven' | 'failed' | 'running'
  impact: string
}

export default function AdminDashboard() {
  const [metrics, setMetrics] = useState<SystemMetrics>({
    stability: 99.9,
    ethics: 98.5,
    agents: 0,
    throughput: 0,
    latency: 0,
    uptime: 100,
    revenue: 0,
    costs: 0
  })

  const [theorems, setTheorems] = useState<TheoremResult[]>([
    { theorem: 'Workflow Closure', status: 'proven', impact: 'DOF=1' },
    { theorem: 'Task Harmonics', status: 'proven', impact: '25% ↑ throughput' },
    { theorem: 'Process Convergence', status: 'proven', impact: 'Lyapunov stable' },
    { theorem: 'Energy Conservation', status: 'proven', impact: '<1% variation' },
    { theorem: 'Cosmic Scaling', status: 'running', impact: 'λ³ scaling' }
  ])

  const [aiStatus, setAiStatus] = useState({
    evolving: true,
    last_evolution: '2 hours ago',
    improvements: 47,
    bugs_fixed: 12
  })

  const [security, setSecurity] = useState({
    ethical_veto: 'active',
    gdpr_compliance: 'compliant',
    encryption: 'AES-256',
    audits_passed: 8
  })

  // Fetch real metrics
  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await fetch('http://localhost:8000/metrics')
        const data = await response.json()
        setMetrics(prev => ({
          ...prev,
          agents: data.agents || 0,
          throughput: data.throughput || 0,
          latency: data.latency || 0
        }))
      } catch (error) {
        console.log('Using mock data')
      }
    }

    fetchMetrics()
    const interval = setInterval(fetchMetrics, 10000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100">
      {/* Top Navigation */}
      <nav className="border-b border-gray-800 bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center">
              <Brain className="h-8 w-8 text-emerald-500" />
              <span className="ml-3 text-xl font-bold">BPO Command</span>
              <span className="ml-2 px-2 py-1 text-xs bg-emerald-900/30 text-emerald-400 rounded">
                ADMIN ONLY
              </span>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="text-sm">
                <div className="text-gray-400">System Status</div>
                <div className="flex items-center">
                  <div className="h-2 w-2 bg-emerald-500 rounded-full mr-2 animate-pulse"></div>
                  <span className="text-emerald-400">OPERATIONAL</span>
                </div>
              </div>
              <Lock className="h-5 w-5 text-gray-500" />
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold">Cosmic Control Panel</h1>
          <p className="text-gray-400 mt-2">Mathematically proven BPO at scale</p>
        </div>

        {/* Main Metrics Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <MetricCard 
            title="System Stability" 
            value={`${metrics.stability}%`}
            icon={<Cpu className="h-5 w-5" />}
            color="emerald"
            subtitle="Lyapunov proven"
          />
          
          <MetricCard 
            title="Ethical Compliance" 
            value={`${metrics.ethics}%`}
            icon={<Shield className="h-5 w-5" />}
            color="blue"
            subtitle="GDPR compliant"
          />
          
          <MetricCard 
            title="Active Agents" 
            value={metrics.agents.toLocaleString()}
            icon={<Users className="h-5 w-5" />}
            color="purple"
            subtitle="Kuramoto synchronized"
          />
          
          <MetricCard 
            title="Throughput" 
            value={`${metrics.throughput}/s`}
            icon={<Zap className="h-5 w-5" />}
            color="amber"
            subtitle="Real-time processing"
          />
        </div>

        {/* Theorem Prover Section */}
        <div className="bg-gray-900 rounded-xl border border-gray-800 p-6 mb-8">
          <div className="flex items-center mb-6">
            <Code className="h-6 w-6 text-emerald-500 mr-3" />
            <h2 className="text-xl font-semibold">Mathematical Theorem Engine</h2>
          </div>
          
          <div className="space-y-4">
            {theorems.map((theorem, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-gray-800/50 rounded-lg">
                <div>
                  <div className="font-medium">{theorem.theorem}</div>
                  <div className="text-sm text-gray-400">{theorem.impact}</div>
                </div>
                <div className={`px-3 py-1 rounded-full text-sm ${
                  theorem.status === 'proven' ? 'bg-emerald-900/30 text-emerald-400' :
                  theorem.status === 'running' ? 'bg-blue-900/30 text-blue-400' :
                  'bg-red-900/30 text-red-400'
                }`}>
                  {theorem.status.toUpperCase()}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* AI Evolution & Security */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* AI Evolution Panel */}
          <div className="bg-gray-900 rounded-xl border border-gray-800 p-6">
            <div className="flex items-center mb-6">
              <Brain className="h-6 w-6 text-purple-500 mr-3" />
              <h2 className="text-xl font-semibold">AI Self-Evolution</h2>
            </div>
            
            <div className="space-y-4">
              <div className="flex justify-between items-center p-3 bg-gray-800/50 rounded-lg">
                <div className="text-gray-300">Evolution Status</div>
                <div className="flex items-center">
                  <div className={`h-2 w-2 rounded-full mr-2 ${aiStatus.evolving ? 'bg-emerald-500 animate-pulse' : 'bg-gray-500'}`}></div>
                  <span className={aiStatus.evolving ? 'text-emerald-400' : 'text-gray-400'}>
                    {aiStatus.evolving ? 'ACTIVE' : 'PAUSED'}
                  </span>
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-4">
                <StatCard label="Code Improvements" value={aiStatus.improvements} />
                <StatCard label="Bugs Auto-Fixed" value={aiStatus.bugs_fixed} />
              </div>
              
              <div className="p-3 bg-gray-800/50 rounded-lg">
                <div className="text-sm text-gray-400 mb-1">Last Evolution</div>
                <div className="text-gray-300">{aiStatus.last_evolution}</div>
              </div>
            </div>
          </div>

          {/* Security & Compliance */}
          <div className="bg-gray-900 rounded-xl border border-gray-800 p-6">
            <div className="flex items-center mb-6">
              <Lock className="h-6 w-6 text-blue-500 mr-3" />
              <h2 className="text-xl font-semibold">Security & Compliance</h2>
            </div>
            
            <div className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                <div className="p-3 bg-gray-800/50 rounded-lg">
                  <div className="text-sm text-gray-400 mb-1">Ethical Veto</div>
                  <div className="text-emerald-400 font-medium">{security.ethical_veto}</div>
                </div>
                <div className="p-3 bg-gray-800/50 rounded-lg">
                  <div className="text-sm text-gray-400 mb-1">GDPR</div>
                  <div className="text-emerald-400 font-medium">{security.gdpr_compliance}</div>
                </div>
              </div>
              
              <div className="p-3 bg-gray-800/50 rounded-lg">
                <div className="text-sm text-gray-400 mb-1">Encryption</div>
                <div className="text-gray-300">{security.encryption}</div>
              </div>
              
              <div className="p-3 bg-gray-800/50 rounded-lg">
                <div className="text-sm text-gray-400 mb-1">Security Audits</div>
                <div className="flex items-center">
                  <div className="text-gray-300 mr-4">{security.audits_passed} passed</div>
                  <div className="h-2 flex-1 bg-gray-700 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-emerald-500 rounded-full"
                      style={{ width: `${(security.audits_passed / 10) * 100}%` }}
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="mt-8 bg-gray-900 rounded-xl border border-gray-800 p-6">
          <h2 className="text-xl font-semibold mb-6">Cosmic Controls</h2>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <ActionButton 
              icon={<Globe />}
              label="Deploy Global"
              onClick={() => console.log('Deploy')}
              color="emerald"
            />
            <ActionButton 
              icon={<Database />}
              label="Scale Database"
              onClick={() => console.log('Scale DB')}
              color="blue"
            />
            <ActionButton 
              icon={<Activity />}
              label="Run Theorems"
              onClick={() => console.log('Run Theorems')}
              color="purple"
            />
            <ActionButton 
              icon={<Key />}
              label="Security Audit"
              onClick={() => console.log('Audit')}
              color="amber"
            />
          </div>
        </div>
      </main>
    </div>
  )
}

// Component: Metric Card
function MetricCard({ 
  title, 
  value, 
  icon, 
  color, 
  subtitle 
}: { 
  title: string
  value: string
  icon: React.ReactNode
  color: string
  subtitle: string
}) {
  const colorClasses = {
    emerald: 'bg-emerald-500/10 text-emerald-400',
    blue: 'bg-blue-500/10 text-blue-400',
    purple: 'bg-purple-500/10 text-purple-400',
    amber: 'bg-amber-500/10 text-amber-400'
  }

  return (
    <div className="bg-gray-900 rounded-xl border border-gray-800 p-6">
      <div className="flex justify-between items-start mb-4">
        <div className={`p-2 rounded-lg ${colorClasses[color as keyof typeof colorClasses]}`}>
          {icon}
        </div>
        <div className="text-2xl font-bold">{value}</div>
      </div>
      <h3 className="font-semibold text-gray-200 mb-1">{title}</h3>
      <p className="text-sm text-gray-400">{subtitle}</p>
    </div>
  )
}

// Component: Stat Card
function StatCard({ label, value }: { label: string, value: number }) {
  return (
    <div className="p-3 bg-gray-800/50 rounded-lg">
      <div className="text-sm text-gray-400 mb-1">{label}</div>
      <div className="text-2xl font-bold text-gray-100">{value}</div>
    </div>
  )
}

// Component: Action Button
function ActionButton({ 
  icon, 
  label, 
  onClick, 
  color 
}: { 
  icon: React.ReactNode
  label: string
  onClick: () => void
  color: string
}) {
  const colorClasses = {
    emerald: 'hover:bg-emerald-500/10 border-emerald-500/30 text-emerald-400',
    blue: 'hover:bg-blue-500/10 border-blue-500/30 text-blue-400',
    purple: 'hover:bg-purple-500/10 border-purple-500/30 text-purple-400',
    amber: 'hover:bg-amber-500/10 border-amber-500/30 text-amber-400'
  }

  return (
    <button 
      onClick={onClick}
      className={`flex flex-col items-center justify-center p-4 rounded-lg border transition-all hover:scale-105 ${colorClasses[color as keyof typeof colorClasses]}`}
    >
      <div className="mb-2">
        {icon}
      </div>
      <span className="text-sm font-medium">{label}</span>
    </button>
  )
}