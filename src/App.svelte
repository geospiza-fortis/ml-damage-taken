<script>
  import Character from "./components/Character.svelte";
  import Mob from "./components/Mob.svelte";
  import DamageTaken from "./components/DamageTaken.svelte";

  let mob = {};
</script>

<main>
  <h1>Damage Taken Calculator</h1>

  <div class="row">
    <div class="col-sm">
      <!--h2 character data-->
      <Character />
    </div>
    <div class="col-sm">
      <!--h2 mob data-->
      <Mob bind:this={mob} />
    </div>
    <div class="col-sm">
      <DamageTaken {mob} />
    </div>
  </div>
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
    padding-bottom: 2em;
  }
</style>
