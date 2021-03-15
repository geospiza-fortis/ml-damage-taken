<script>
  import Character from "./components/Character.svelte";
  import Mob from "./components/Mob.svelte";
  import DamageTaken from "./components/DamageTaken.svelte";
  import Plot from "./components/Plot.svelte";

  let mob = {};
  let dealWeaponDamage;
  let dealMagicDamage;

  function unif(min, max) {
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

  // e.g. sample(dealWeaponDamage, () => rand(0.008, 0.0085))
  function sample(dealDamage, rand = () => 0.5, samples = 10000) {
    let data = [];
    for (let i = 0; i < samples; i++) {
      data.push(dealDamage(rand()));
    }
    return data;
  }

  function sampleWeaponDamage() {
    weapon_damage = sample(dealWeaponDamage, () => unif(0.008, 0.0085));
  }

  function sampleMagicDamage() {
    magic_damage = sample(dealMagicDamage, () => unif(0.0075, 0.008));
  }

  let weapon_damage = [];
  let magic_damage = [];
  // initial plots
  $: dealWeaponDamage && sampleWeaponDamage();
  $: dealMagicDamage && sampleMagicDamage();
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
  <h2>Plots</h2>

  <div class="row">
    <div class="col-md">
      <button on:click={sampleWeaponDamage}>Resample and Plot</button>

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
    <div class="col-md">
      <button on:click={sampleMagicDamage}>Resample and Plot</button>

      {#if magic_damage.length}
        <Plot
          data={magic_damage}
          {transform}
          layout={{
            title: `histogram of magic damage taken (n=${magic_damage.length})`,
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
