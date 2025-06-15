export function LinkTextBox() {
  return (
    <div className="w-full max-w-md flex">
      <div className="bg-white rounded-l-xl shadow-md w-full max-w-md">
        <input
          type="url"
          placeholder="Enter your Github Repo URL"
          className="w-full p-3 border border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out"
        ></input>
      </div>
      <div className="bg-white rounded-r-xl ml-0">
        <button className="w-full h-full border border-gray-300 rounded-r-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-center text-gray-800 p-3 transition duration-200 ease-in-out">
          Submit
        </button>
      </div>
    </div>
  );
}
