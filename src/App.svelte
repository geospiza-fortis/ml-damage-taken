<script>
  import Character from "./components/Character.svelte";
  import Mob from "./components/Mob.svelte";
  import DamageTaken from "./components/DamageTaken.svelte";
  import Plot from "./components/Plot.svelte";

  let mob = {};
  let dealWeaponDamage;
  let dealMagicDamage;

  function rand(min, max) {
    return Math.random() * (max - min) + min;
  }

  function transform(data) {
    return [
      {
        x: data,
        type: "histogram",
      },
    ];
  }

  let samples = 10000;
  let weapon_damage = [];
  function sample() {
    weapon_damage = [];
    for (let i = 0; i < samples; i++) {
      weapon_damage.push(dealWeaponDamage(rand(0.008, 0.0085)));
    }
    weapon_damage = [...weapon_damage];
  }
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
      <DamageTaken {mob} bind:dealWeaponDamage bind:dealMagicDamage />
    </div>
  </div>
  <div class="row">
    <div class="col">
      <h2>Plots</h2>
      <button on:click={sample}>Sample and Plot</button>

      {#if weapon_damage.length}
        <Plot
          data={weapon_damage}
          {transform}
          layout={{
            title: `histogram of weapon damage taken (n=${weapon_damage.length})`,
          }}
        />
      {/if}
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
