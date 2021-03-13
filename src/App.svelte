<script>
  const jobs = ["beginner", "bowman", "magician", "warrior", "thief", "pirate"];
  export let job = "beginner";
</script>

<main>
  <h1>Calculator</h1>
  <h2>Character</h2>
  <input bind:value={job} />
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  }
</style>
