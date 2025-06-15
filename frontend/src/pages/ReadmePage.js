import { useLocation } from "react-router-dom";

export function ReadMePage() {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const repoUrl = searchParams.get("repo");

  return <h1>{repoUrl}</h1>;
}
