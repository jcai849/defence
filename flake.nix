{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  outputs =
    { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default =
        with pkgs;
        mkShell {
          buildInputs = [
            nodejs
            importNpmLock.hooks.linkNodeModulesHook
            superhtml
            typescript-language-server
            dot-language-server
            gnumake
            svgbob
            plantuml
            uv
          ];

          npmDeps = importNpmLock.buildNodeModules {
            npmRoot = ./.;
            inherit nodejs;
          };

          shellHook = "${pkgs.gnumake}/bin/make";
        };
    };
}
