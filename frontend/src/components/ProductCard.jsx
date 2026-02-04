import React from 'react';
import Comentarios from './Comments';

export default function App() {
  return (
    <div className="min-h-screen w-full text-white p-6">
      <div className="w-full">
        <div className="w-full bg-gray-800 rounded-2xl shadow-lg p-6 mb-8">
          <img
            src="https://placehold.co/200x300"
            alt="Produto"
            className="rounded-xl w-full h-64 object-cover mb-4"
          />
          <h1 className="text-3xl font-bold mb-2">Camisa SciTec Jr.</h1>
          <p className="text-xl text-green-400 mb-1">R$ 49,90</p>
          <p className="text-sm text-gray-400 mb-4">Produto satisfatório</p>

          <div className="mb-4">
            <details className="bg-gray-700 rounded-lg p-4 cursor-pointer">
              <summary className="font-semibold mb-2">Descrição</summary>
              <p className="text-sm mt-2">Camisa confortável, bonita, perfeita para usar no dia a dia.</p>
            </details>
          </div>

          <div className="mb-2">
            <p><span className="font-semibold">ID:</span> 24052006</p>
            <p><span className="font-semibold">Estoque:</span> 17 unidades</p>
          </div>

          <div className="grid grid-cols-2 gap-4 mt-4">
            <div>
              <label className="block mb-1">Tamanho</label>
              <select className="w-full bg-gray-700 rounded p-2">
                <option>PP</option>
                <option>P</option>
                <option>M</option>
                <option>G</option>
                <option>GG</option>
              </select>
            </div>
            <div>
              <label className="block mb-1">Cor</label>
              <select className="w-full bg-gray-700 rounded p-2">
                <option>Preto</option>
                <option>Cinza</option>
                <option>Azul</option>
              </select>
            </div>
          </div>
        </div>

        <Comentarios />
      </div>
    </div>
  );
}
