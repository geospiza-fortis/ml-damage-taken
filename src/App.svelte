<script>
  import Character from "./components/Character.svelte";
  let char = {};
</script>

<main>
  <h1>Calculator</h1>

  <Character bind:this={char} />

  {char.hp}
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  }
</style>
