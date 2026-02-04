import { useEffect, useState } from "react";

export default function Comentarios() {
  const [comentarios, setComentarios] = useState([]);
  const [novoComentario, setNovoComentario] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/api/comentarios")
      .then((res) => res.json())
      .then((data) => setComentarios(data))
      .catch((err) => console.error("Erro ao carregar comentários:", err));
  }, []);

  const enviarComentario = () => {
    if (!novoComentario.trim()) return;

    fetch("http://localhost:5000/api/comentarios", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ texto: novoComentario }),
    })
      .then((res) => {
        if (res.ok) {
          return fetch("http://localhost:5000/api/comentarios")
            .then((res) => res.json())
            .then((data) => {
              setComentarios(data);
              setNovoComentario("");
            });
        } else {
          console.error("Erro ao enviar comentário");
        }
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="w-full mt-10 bg-zinc-800 p-6 rounded-2xl shadow-xl text-white">
      <h2 className="text-2xl font-semibold mb-4">Comentários</h2>

      {comentarios.length === 0 ? (
        <p className="text-gray-400">Nenhum comentário ainda.</p>
      ) : (
        <div className="space-y-4">
          {comentarios.map((comentario) => (
            <div key={comentario.id} className="border-b border-zinc-700 pb-2">
              <p className="text-sm text-gray-400">{new Date(comentario.hora).toLocaleString()}</p>
              <p className="text-base">{comentario.texto}</p>
            </div>
          ))}
        </div>
      )}

      <div className="mt-6">
        <textarea
          className="w-full p-2 rounded bg-zinc-700 text-white resize-none"
          rows="3"
          placeholder="Escreva seu comentário..."
          value={novoComentario}
          onChange={(e) => setNovoComentario(e.target.value)}
        />
        <button
          onClick={enviarComentario}
          className="mt-2 bg-indigo-600 hover:bg-indigo-500 px-4 py-2 rounded text-white"
        >
          Enviar
        </button>
      </div>
    </div>
  );
}
