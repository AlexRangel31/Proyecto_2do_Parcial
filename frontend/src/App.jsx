import { useEffect, useState } from 'react'
import ContactForm from './components/ContactForm'
import ContactList from './components/ContactList'
import DeleteForm from './components/DeleteForm'

function App() {
  const [contactos, setContactos] = useState([])

  const cargarContactos = async () => {
    const res = await fetch('/api/contactos')
    const data = await res.json()
    setContactos(data)
  }

  useEffect(() => {
    cargarContactos()
  }, [])

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Agenda de Contactos</h1>
      <ContactForm onAdd={cargarContactos} />
      <DeleteForm onDelete={cargarContactos} />
      <ContactList contactos={contactos} />
    </div>
  )
}

export default App