import React, { useEffect, useState } from 'react'

export default function App(){
  const [messages, setMessages] = useState({gmail:[], outlook:[], whatsapp:[], unified:[]})

  useEffect(()=>{
    fetch('/api/messages/all').then(r=>r.json()).then(setMessages).catch(()=>{})
  },[])

  return (
    <div style={{fontFamily:'Arial, sans-serif', padding:20}}>
      <h1>Inbox Unificada - Demo</h1>
      <p>Esta é uma UI mínima. Integração com backend via /api/messages/*</p>
      <section>
        <h2>Unificada (exemplo)</h2>
        <ul>
          {messages.unified && messages.unified.slice(0,50).map(m=> (
            <li key={m.id}><strong>{m.source}</strong> - {m.from} - {m.subject || m.snippet} - {m.date}</li>
          ))}
        </ul>
      </section>
    </div>
  )
}
